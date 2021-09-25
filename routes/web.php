<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('home');
});

Route::get('/newpoints', function () {
    return view('newpoints');
});

Route::get('/menu', function () {
    return view('menu');
});

Route::get('/bonuses', function () {
    return view('bonuses');
});


Route::get('/phpinfo', function () {
    return phpinfo();
});

Route::get('/pay', function () {
    return view('pay');
});

Route::get('/validate', function () {
    return view('validate');
});