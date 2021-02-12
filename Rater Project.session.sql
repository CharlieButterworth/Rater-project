INSERT INTO django_admin_log (
        id,
        action_time,
        object_id,
        object_repr,
        change_message,
        content_type_id,
        user_id,
        action_flag
    )
VALUES (
        id :integer,
        'action_time:datetime',
        'object_id:text',
        'object_repr:varchar(200)',
        'change_message:text',
        content_type_id :integer,
        user_id :integer,
        'action_flag:smallint unsigned'
    );
delete from django_migrations
where app = "raterapi"