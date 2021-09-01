// Mars lander simulator
// Version 1.10
// Mechanical simulation functions
// Gabor Csanyi and Andrew Gee, August 2017

// Permission is hereby granted, free of charge, to any person obtaining
// a copy of this software and associated documentation, to make use of it
// for non-commercial purposes, provided that (a) its original authorship
// is acknowledged and (b) no modified versions of the source code are
// published. Restriction (b) is designed to protect the integrity of the
// exercise for future generations of students. The authors would be happy
// to receive any suggested modifications by private correspondence to
// ahg@eng.cam.ac.uk and gc121@eng.cam.ac.uk.

#include "lander.h"

void autopilot (void)
  // Autopilot to adjust the engine throttle, parachute and attitude control
{
  // INSERT YOUR CODE HERE
	double K_h;
	double K_p;
	double error_vel;
	double altitude;
	double P_out; //output of proportional controller
	double offset;
	

	K_h = 17e-3;
	K_p = 1.8;
	offset = 0.3;

	altitude = position.abs() - MARS_RADIUS;
	//cout << altitude << endl;
	error_vel = -(0.5 + K_h * altitude + velocity * position.norm());
	P_out = K_p * error_vel;

	if (P_out <= - offset) {
		throttle = 0.0;
	}
	else if (P_out >= 1 - offset) {
		throttle = 1.0;
	}
	else {
		throttle = offset + P_out;
	}

	//output data to a file for plotting
	ofstream fout;
	ifstream fin;
	fin.open("results.txt");
	fout.open("results.txt", ios::app); //append mode
	if (fin.is_open()) {
		fout << simulation_time << " " << altitude << " " << velocity * position.norm() << endl;
		cout << "written" << endl;
	}
}

void numerical_dynamics (void)
  // This is the function that performs the numerical integration to update the
  // lander's pose. The time step is delta_t (global variable).
{
  // INSERT YOUR CODE HERE
  
  //euler
  
  //verlet
	static vector3d previous_position;
	vector3d new_position;
	vector3d force_total;
	vector3d force_gravity;
	vector3d thrust;
	vector3d force_drag_lander;
	vector3d force_drag_chute;
	double mass_lander;
	double d;
	double area_lander;
	double area_chute;
	vector3d a;

	mass_lander = UNLOADED_LANDER_MASS + fuel * FUEL_CAPACITY * FUEL_DENSITY;
	force_gravity = -(GRAVITY * MARS_MASS * mass_lander / position.abs2()) * position.norm();
	thrust = thrust_wrt_world();
	d = atmospheric_density(position);
	area_lander = M_PI * LANDER_SIZE * LANDER_SIZE;
	force_drag_lander = -(0.5 * d * DRAG_COEF_LANDER * area_lander * velocity.abs2()) * velocity.norm();
	area_chute = 20.0 * LANDER_SIZE * LANDER_SIZE;
	force_drag_chute = -(0.5 * d * DRAG_COEF_CHUTE * area_chute * velocity.abs2()) * velocity.norm();

	if (parachute_status == DEPLOYED) {
		force_total = force_gravity + thrust + force_drag_chute + force_drag_lander;
	}
	else if (parachute_status == NOT_DEPLOYED or parachute_status == LOST) {
		force_total = force_gravity + thrust + force_drag_lander;
	}

	/*a = force_total / mass_lander;
	new_position = position + delta_t * velocity;
	velocity = velocity + delta_t * a;

	position = new_position;*/
	//cout << velocity << endl;
	//cout <<  << endl;

	if (simulation_time == 0.0) {
	  // euler
		
		a = force_total / mass_lander;
		new_position = position + delta_t * velocity;
		velocity = velocity + delta_t * a;
	}
	else {
      // verlet
		
		a = force_total / mass_lander;
		new_position = 2 * position - previous_position + (delta_t) * (delta_t) * a;
		velocity = (new_position - previous_position) / (2 * delta_t);
	}

	previous_position = position;
	position = new_position;
		

  // Here we can apply an autopilot to adjust the thrust, parachute and attitude
  if (autopilot_enabled) autopilot();

  // Here we can apply 3-axis stabilization to ensure the base is always pointing downwards
  if (stabilized_attitude) attitude_stabilization();
}

void initialize_simulation (void)
  // Lander pose initialization - selects one of 10 possible scenarios
{
  // The parameters to set are:
  // position - in Cartesian planetary coordinate system (m)
  // velocity - in Cartesian planetary coordinate system (m/s)
  // orientation - in lander coordinate system (xyz Euler angles, degrees)
  // delta_t - the simulation time step
  // boolean state variables - parachute_status, stabilized_attitude, autopilot_enabled
  // scenario_description - a descriptive string for the help screen

  scenario_description[0] = "circular orbit";
  scenario_description[1] = "descent from 10km";
  scenario_description[2] = "elliptical orbit, thrust changes orbital plane";
  scenario_description[3] = "polar launch at escape velocity (but drag prevents escape)";
  scenario_description[4] = "elliptical orbit that clips the atmosphere and decays";
  scenario_description[5] = "descent from 200km";
  scenario_description[6] = "";
  scenario_description[7] = "";
  scenario_description[8] = "";
  scenario_description[9] = "";

  switch (scenario) {

  case 0:
    // a circular equatorial orbit
    position = vector3d(1.2*MARS_RADIUS, 0.0, 0.0);
    velocity = vector3d(0.0, -3247.087385863725, 0.0);
    orientation = vector3d(0.0, 90.0, 0.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = false;
    autopilot_enabled = false;
    break;

  case 1:
    // a descent from rest at 10km altitude
    position = vector3d(0.0, -(MARS_RADIUS + 10000.0), 0.0);
    velocity = vector3d(0.0, 0.0, 0.0);
    orientation = vector3d(0.0, 0.0, 90.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = true;
    autopilot_enabled = false;
    break;

  case 2:
    // an elliptical polar orbit
    position = vector3d(0.0, 0.0, 1.2*MARS_RADIUS);
    velocity = vector3d(3500.0, 0.0, 0.0);
    orientation = vector3d(0.0, 0.0, 90.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = false;
    autopilot_enabled = false;
    break;

  case 3:
    // polar surface launch at escape velocity (but drag prevents escape)
    position = vector3d(0.0, 0.0, MARS_RADIUS + LANDER_SIZE/2.0);
    velocity = vector3d(0.0, 0.0, 5027.0);
    orientation = vector3d(0.0, 0.0, 0.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = false;
    autopilot_enabled = false;
    break;

  case 4:
    // an elliptical orbit that clips the atmosphere each time round, losing energy
    position = vector3d(0.0, 0.0, MARS_RADIUS + 100000.0);
    velocity = vector3d(4000.0, 0.0, 0.0);
    orientation = vector3d(0.0, 90.0, 0.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = false;
    autopilot_enabled = false;
    break;

  case 5:
    // a descent from rest at the edge of the exosphere
    position = vector3d(0.0, -(MARS_RADIUS + EXOSPHERE), 0.0);
    velocity = vector3d(0.0, 0.0, 0.0);
    orientation = vector3d(0.0, 0.0, 90.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = true;
    autopilot_enabled = false;
    break;

  case 6:
    break;

  case 7:
    break;

  case 8:
    break;

  case 9:
    break;

  }
}
