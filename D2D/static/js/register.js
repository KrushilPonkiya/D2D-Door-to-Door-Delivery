function userType() {
    let registerForm = document.getElementById('registerForm');
    let str;
    if (document.getElementById('user').checked == true) {
        console.log('user is checked');
        str = `<div class="userRegForm" data-aos="flip-up" data-aos-delay="100">
                        <input type="text" class="form-control mb-0" name="username" placeholder="username">
                        <div class="row">
                            <div class="col">
                                <input type="text" class="form-control" name="firstname"
                                    placeholder="First Name">

                            </div>
                            <div class="col">
                                <input type="text" class="form-control" name="lastname" placeholder="Last Name">

                            </div>
                        </div>


                        <input type="email" class="form-control mt-0" name="email" placeholder="Email">
                        <input type="number" class="form-control" pattern="[7-9]{1}[0-9]{9}" name="number" placeholder="Contact number" required>
                        <input type="password" class="form-control" name="pass1" placeholder="Password">
                        <input type="password" class="form-control" name="pass2"
                            placeholder="Confirm Password">
                    </div>`;

    } else if (document.getElementById('delivery_person').checked == true) {
        console.log('deliveryperson');
        str = `<div class="deliveryRegForm" data-aos="flip-up" data-aos-delay="100">
        <input type="text" class="form-control mb-0" name="user_username" placeholder="username">

                        <div class="row">
                            <div class="col">
                                <input type="text" class="form-control mb-1" name="firstname"
                                    placeholder="First Name">

                            </div>
                            <div class="col">
                                <input type="text" class="form-control mb-1" name="lastname"
                                    placeholder="Last">

                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <input type="email" class="form-control mb-1" name="email" placeholder="Email">
                            </div>
                            <div class="col">
                                <input type="number" class="form-control mb-1" pattern="[7-9]{1}[0-9]{9}" name="number"
                                    placeholder="Contact number">

                            </div>
                        </div>

                        <input type="text" class="form-control mb-1" name="address" placeholder="Address">
                        <div class="row">
                            <div class="col">
                                <input type="number" class="form-control mb-1" name="aadhar" placeholder="Aadhar number">
                            </div>
                            <div class="col">
                                <input type="text" class="form-control mb-1" name="PAN" placeholder="PAN number">
                            </div>
                        </div>

                        <div class="row">
                            <div class="col">
                                <input type="text" class="form-control mb-1" name="driving_licence" placeholder="Driving licence number">
                            </div>
                            <div class="col">
                                <input type="text" class="form-control mb-1" name="vehicle_rc" placeholder="Vehicle RC number">
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <input type="password" class="form-control mb-1" name="pass1"
                                    placeholder="Password">

                            </div>
                            <div class="col">
                                <input type="password" class="form-control mb-1" name="pass2"
                                    placeholder="Confirm Password">

                            </div>
                        </div>
                    </div>`;
    }
    registerForm.innerHTML = str;
}