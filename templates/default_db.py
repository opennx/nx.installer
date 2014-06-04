DB_TEMPLATE = [

"""CREATE EXTENSION IF NOT EXISTS unaccent WITH SCHEMA public;""",

"""CREATE TABLE "public"."nx_settings" ( 
    "key" varchar(50) NOT NULL, 
    "value" text NOT NULL, 
    CONSTRAINT "nx_settings_pkey" PRIMARY KEY ("key")
);""",


"""CREATE TABLE "public"."nx_items" ( 
    "id_object" serial NOT NULL, 
    "id_asset" integer NOT NULL, 
    "id_bin" integer NOT NULL, 
    "position" integer NOT NULL, 
    "ctime" integer NOT NULL, 
    "mtime" integer NOT NULL, 
    CONSTRAINT "PK_nx_items" PRIMARY KEY ("id_object")
)""",


"""CREATE TABLE "public"."nx_bins" ( 
    "id_object" serial NOT NULL, 
    "bin_type" integer NOT NULL, 
    "ctime" integer NOT NULL, 
    "mtime" integer NOT NULL, 
    CONSTRAINT "PK_nx_bins" PRIMARY KEY ("id_object")
)""",


"""CREATE TABLE "public"."nx_assets" ( 
    "id_object" serial NOT NULL, 
    "media_type" integer NOT NULL, 
    "content_type" integer NOT NULL, 
    "id_folder" integer NOT NULL, 
    "origin" varchar(50) NOT NULL, 
    "version_of" integer NOT NULL, 
    "status" integer NOT NULL, 
    "ctime" integer NOT NULL, 
    "mtime" integer NOT NULL, 
    CONSTRAINT "nx_assets_pkey" PRIMARY KEY ("id_object")
)""",


"""CREATE TABLE "public"."nx_meta" ( 
    "id_object" integer NOT NULL, 
    "object_type" integer NOT NULL, 
    "tag" varchar(50) NOT NULL, 
    "value" text NOT NULL, 
    CONSTRAINT "PK_nx_meta" PRIMARY KEY ("tag", "id_object", "object_type")
)""",


"""CREATE TABLE "public"."nx_events" ( 
    "id_object" serial NOT NULL, 
    "start" integer NOT NULL, 
    "stop" integer NOT NULL, 
    "id_channel" integer NOT NULL, 
    "id_magic" integer NOT NULL, 
    "ctime" integer NOT NULL, 
    "mtime" integer NOT NULL, 
    CONSTRAINT "PK_nx_events" PRIMARY KEY ("id_object")
)""",


"""CREATE TABLE "public"."nx_folders" ( 
    "id_folder" serial NOT NULL, 
    "title" varchar(50) NOT NULL, 
    "color" integer NOT NULL, 
    CONSTRAINT "nx_folders_pkey" PRIMARY KEY ("id_folder")
)""",


"""CREATE TABLE "public"."nx_services" ( 
    "id_service" serial NOT NULL, 
    "agent" varchar(50) NOT NULL, 
    "title" varchar(50) NOT NULL, 
    "host" varchar(50) NOT NULL, 
    "autostart" integer NOT NULL, 
    "loop_delay" integer NOT NULL, 
    "settings" text NULL, 
    "state" integer NOT NULL, 
    "pid" integer NOT NULL, 
    "last_seen" integer NOT NULL, 
    CONSTRAINT "nx_services_pkey" PRIMARY KEY ("id_service")
)""",


"""CREATE TABLE "public"."nx_storages" ( 
    "id_storage" serial NOT NULL, 
    "title" varchar(50) NOT NULL, 
    "protocol" integer NOT NULL, 
    "path" varchar(255) NOT NULL, 
    "login" varchar(50) NOT NULL, 
    "password" varchar(50) NOT NULL, 
    CONSTRAINT "nx_storages_pkey" PRIMARY KEY ("id_storage")
)""",


"""CREATE TABLE "public"."nx_channels" ( 
    "id_channel" serial NOT NULL, 
    "channel_type" integer NOT NULL, 
    "title" varchar(50) NOT NULL, 
    "config" text NOT NULL, 
    CONSTRAINT "PK_nx_channels" PRIMARY KEY ("id_channel")
)""",


"""CREATE TABLE "public"."nx_actions" ( 
    "id_action" serial NOT NULL, 
    "title" varchar(50) NOT NULL, 
    "config" text NOT NULL, 
    CONSTRAINT "PK_nx_actions" PRIMARY KEY ("id_action")
)""",


"""CREATE TABLE "public"."nx_jobs" ( 
    "id_job" serial NOT NULL, 
    "id_object" integer NOT NULL, 
    "id_action" integer NOT NULL, 
    "settings" text NULL, 
    "id_service" integer NOT NULL, 
    "priority" integer NOT NULL, 
    "progress" integer NOT NULL, 
    "retries" integer NOT NULL, 
    "ctime" integer NOT NULL, 
    "stime" integer NOT NULL, 
    "etime" integer NOT NULL, 
    "message" text NOT NULL, 
    "id_user" integer NOT NULL, 
    CONSTRAINT "PK_nx_jobs" PRIMARY KEY ("id_job")
)""",


"""CREATE TABLE "public"."nx_meta_types" ( 
    "namespace" varchar(10) NOT NULL, 
    "tag" varchar(50) NOT NULL, 
    "editable" integer NOT NULL, 
    "searchable" integer NOT NULL, 
    "class" integer NOT NULL, 
    "default_value" text NOT NULL, 
    "settings" text NOT NULL, 
    CONSTRAINT "nx_meta_types_pkey" PRIMARY KEY ("tag")
)""",


"""CREATE TABLE "public"."nx_meta_aliases" ( 
    "tag" varchar(50) NOT NULL, 
    "lang" varchar(50) NOT NULL, 
    "alias" varchar(50) NOT NULL, 
    "col_header" varchar(50) NULL, 
    CONSTRAINT "nx_meta_aliases_pkey" PRIMARY KEY ("tag", "lang")
)""",


"""CREATE TABLE "public"."nx_views" ( 
    "id_view" serial NOT NULL, 
    "title" varchar(50) NOT NULL, 
    "owner" integer NOT NULL DEFAULT 0, 
    "config" text NOT NULL, 
    "position" integer NOT NULL DEFAULT 0, 
    CONSTRAINT "PK_nx_views" PRIMARY KEY ("id_view")
)"""

]


