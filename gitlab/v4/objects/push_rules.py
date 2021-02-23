from gitlab.base import *  # noqa
from gitlab.mixins import *  # noqa


__all__ = [
    "GroupPushRules",
    "GroupPushRulesManager",
    "ProjectPushRules",
    "ProjectPushRulesManager",
]


class GroupPushRules(SaveMixin, ObjectDeleteMixin, RESTObject):
    _id_attr = None


class GroupPushRulesManager(
    GetWithoutIdMixin, CreateMixin, UpdateMixin, DeleteMixin, RESTManager
):
    _path = "/groups/%(group_id)s/push_rule"
    _obj_cls = GroupPushRules
    _from_parent_attrs = {"group_id": "id"}
    _create_attrs = (
        tuple(),
        (
            "deny_delete_tag",
            "member_check",
            "prevent_secrets",
            "commit_message_regex",
            "commit_message_negative_regex",
            "branch_name_regex",
            "author_email_regex",
            "file_name_regex",
            "max_file_size",
            "commit_committer_check",
            "reject_unsigned_commits",
        ),
    )
    _update_attrs = (
        tuple(),
        (
            "deny_delete_tag",
            "member_check",
            "prevent_secrets",
            "commit_message_regex",
            "commit_message_negative_regex",
            "branch_name_regex",
            "author_email_regex",
            "file_name_regex",
            "max_file_size",
            "commit_committer_check",
            "reject_unsigned_commits",
        ),
    )


class ProjectPushRules(SaveMixin, ObjectDeleteMixin, RESTObject):
    _id_attr = None


class ProjectPushRulesManager(
    GetWithoutIdMixin, CreateMixin, UpdateMixin, DeleteMixin, RESTManager
):
    _path = "/projects/%(project_id)s/push_rule"
    _obj_cls = ProjectPushRules
    _from_parent_attrs = {"project_id": "id"}
    _create_attrs = (
        tuple(),
        (
            "author_email_regex",
            "branch_name_regex",
            "commit_committer_check",
            "commit_message_negative_regex",
            "commit_message_regex",
            "deny_delete_tag",
            "file_name_regex",
            "max_file_size",
            "member_check",
            "prevent_secrets",
            "reject_unsigned_commits",
        ),
    )
    _update_attrs = (
        tuple(),
        (
            "author_email_regex",
            "branch_name_regex",
            "commit_committer_check",
            "commit_message_negative_regex",
            "commit_message_regex",
            "deny_delete_tag",
            "file_name_regex",
            "max_file_size",
            "member_check",
            "prevent_secrets",
            "reject_unsigned_commits",
        ),
    )
