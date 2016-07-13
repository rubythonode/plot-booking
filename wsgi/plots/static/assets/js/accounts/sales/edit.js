$(document).ready(function() {
    getBookingDetails();
    $(document).on('click', '#emi', function() {
        var checkbox = this;
        if($(checkbox).is(':checked')){
            $(".emi-div").show();
            $(".payments-div").show();
        }else{
            $(".emi-div").hide();
            $(".payments-div").hide();
        }
    });
});

function getBookingDetails(){
    booking_id = $("#booking_id").val();
    $.get("/api/booking/" + booking_id + "/", function(data, status) {
        customer = data.customer;
        $(".customer-name").text(customer.first_name+" "+customer.middle_name+" "+customer.last_name);
        $(".customer-mobile").text(customer.mobile);
        $(".customer-email").text(customer.email);
        $(".customer-address1").text(customer.address1);
        $(".customer-address2").text(customer.address2);
        $(".customer-pin_code").text(customer.pin_code);
        $(".customer-alternate_mobile").text(customer.alternate_mobile);
        $(".customer-occupation").text(customer.occupation);
        $(".customer-dob").text(customer.dob);
        $(".customer-age").text(customer.age);
        $(".customer-marriage_anniversary").text(customer.marriage_anniversary);
        $(".customer-nominee_name").text(customer.nominee_name);
        $(".customer-relation").text(customer.relation);
        if(customer.photo != null){
            $("#profile-image").attr("src",customer.photo);
        }

        plot = data.plot_no

        $(".plot-project_name").text(plot.project_name);
        $(".plot-facing").text(plot.facing);
        $(".plot-area").text(plot.area);
        $(".plot-width").text(plot.width);
        $(".plot-breadth").text(plot.breadth);
        $(".plot-rate_per_sqft").text(plot.rate_per_sqft);
        $(".plot-survey_no").text(plot.survey_no);
        $(".plot-plot_no").text(plot.plot_no);

        $(".booking_date").text(data.booking_date);
        $(".booking_amount").text(data.booking_amount);

        sale = data.sale_booking[0]

        $(".is_emi_enabled").html(getTrueFalse(sale.is_emi_enabled));
        $(".basic_cost").text(parseInt(sale.basic_cost));
        $(".sales_cost").text(parseInt(sale.sales_cost));
        $(".remaning_cost").text(parseInt(sale.remaning_cost));

        $("#total_amount").val(parseInt(sale.sales_cost));
        $("#booking_amount").val(data.booking_amount);
        $("#booking_amount_method").val(data.booking_amount_method).change();
        $("#booking_date").val(data.booking_date);
        $("#booking_txn_no").val(data.booking_txn_no);
        $("#down_payment").val(data.down_payment);
        $("#down_payment_method").val(data.down_payment_method).change();
        $("#down_payment_date").val(data.down_payment_date);
        $("#loan_amount").val(sale.loan_amount);
        $("#loan_amount_changed").val(sale.loan_amount);


        if(sale.is_emi_enabled){
            $(".emi-div").show();
            $(".payments-div").show();
            emi = sale.emi_sale[0]
            $("#emi").prop('checked', true);
            $("#emi_terms").val(emi.duration).change();
            $("#emi_day").val(emi.emi_day);
            $("#emi_intrest").val(emi.intrest_rate);
            $("#loan_amount").val(parseInt(emi.total_amount));

            emi_installments = emi.emi_data;

            destroyTable("#payments-table");
            table = $('#payments-table').DataTable({
                responsive: true,
                dom: 'Bfrtip',
                buttons: [
                    'print'
                ]
            });

            for(var i=0; i<emi_installments.length; i++){
                em = emi_installments[i]
                emi_status = getTrueFalse(em.paid_status)
                table.row.add([i, em.emi_schedule_date, parseFloat(em.amount).toFixed(2), emi_status]).draw(true);
            }

        }


    });
}

$(document).on('click', '#calculate-emi', function() {
    calculateEMI();
});


function calculateLoanAmount(){
    booking_amount = getValById("booking_amount");
    down_payment = getValById("down_payment");
    total_amount = getValById("total_amount");

    paid_amount = booking_amount + down_payment;

    loan_amount = total_amount - paid_amount;

    $("#loan_amount").val(loan_amount);

    return loan_amount;

}


function calculateEMI(){

    loan_amount = calculateLoanAmount();  
 
    intrest_rate  = getValById("emi_intrest");

    emi_day  = getValById("emi_day");

    duration = parseInt($("#emi_terms option:selected").val());

    emi_amount =  getMonthlyEMI(loan_amount, intrest_rate, duration);

    printEMI(emi_amount, duration, emi_day);

}

function printEMI(emi, duration, emi_day){
    destroyTable("#payments-table");
    table = $('#payments-table').DataTable({
        responsive: true,
        dom: 'Bfrtip',
        buttons: [
            'print'
        ]
    });
    var date = new Date();
    for(var i=1; i<=duration; i++){
        date.setDate(emi_day);
        date.setMonth(date.getMonth() + 1);
        table.row.add([i, date.toLocaleFormat('%d-%b-%Y'), emi.toFixed(2)]).draw(true);
    }
}


function getMonthlyEMI(principle_amount, intrest_rate, duration){

    intrest_rate   = intrest_rate / 1200;

    emi_amount = 0;

    if(intrest_rate == 0){
        emi_amount =  principle_amount / duration;
    }else{
        emi_amount =  principle_amount * intrest_rate / (1 - (Math.pow(1/(1 + intrest_rate), duration)));
    }
    return emi_amount
}

function getTrueFalse(status){
    if(status){
        status = '<label class="tbl-icon icon-true"><i class="fa fa-check" aria-hidden="true"></i></label>';
    }else{
        status = '<label class="tbl-icon icon-false"><i class="fa fa-times " aria-hidden="true"></i></label>';
    }
    return status;
}