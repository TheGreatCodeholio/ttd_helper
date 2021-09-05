<?php /** @noinspection PhpUnhandledExceptionInspection */

/**
 * Database Connection Class
 * @license      Apache License v2.0
 * @author       Smashedbotatos <ian@icarey.net>
 * @copyright    Copyright © 2009-2021 iCarey Computer Services.
 *
 */

class DatabaseConnect
{
    public $con;

    public function __construct($host, $username, $password, $database, $port) {
        $this->con = mysqli_connect($host, $username, $password, $database, $port);
        if(!$this->con) {
            echo '<div class="alert alert-danger" role="alert">Database Connection Failed!</div>';
        }
    }

    public function clean($data) {
        return mysqli_real_escape_string($this->con, $data);
    }

    public function error($error) {
        die($error);
    }

    public function query($query) {
        $result = mysqli_query($this->con, $query) or $this->error($query . ' / ' . mysqli_error($this->con));
        return $result;
    }

    public function fetch($result) {
        return mysqli_fetch_assoc($result);
    }

    public function num_rows($result) {
        return mysqli_num_rows($result);
    }

    public function affected_rows() {
        return mysqli_affected_rows($this->con);
    }

    /**
     * @return mysqli
     */
    public function closeCon()
    {
        global $con;
        mysqli_close($this->$con);

    }
}