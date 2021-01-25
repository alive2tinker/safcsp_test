<?php

/**
 * Assuming that we are using Laravel PHP framework, we can establish the task at hand by doing the following 
 */

 // first we generate the model using artisan cli
 php artisan make:model Comment -m

 //then we write the schema for comment model along with foreign key for user and post models.

//  $table->id();
 $table->longText('message');
 $table->unsignedBigInteger('post_id');
 $table->unsignedBigInteger('user_id');
 $table->foreign('post_id')->references('id')->on('posts')->onDelete('cascade');
 $table->foreign('user_id')->references('id')->on('users')->onDelete('cascade');
//  $table->timestamps()


//then we define relationships between post and comment models like the following

//in post.php
public function comments(){
    return $this->hasMany(Comment::class);
}

//in Comment.php
public function post(){
    return $this->belongsTo(Post::class);
}


//then in the method show() of PostController, we write the following

$post = Post::with('comments')->findOrFail($id);