# -*- coding: utf-8 -*-

from module.django_jsonschema import JSONSchemaModel


class TodoItemSchemaMixin(JSONSchemaModel):

    schema_base = {
        'title': 'todo item',
        'description': '',
        'type': 'object',
        'properties': {
            'id': {
                'type': 'integer',
            },
            'text': {
                'type': 'string',
            },
        },
    }

    def to_dict(self):
        name_list = ['id', 'text']
        return {x: getattr(self, x) for x in name_list}


class TodoListSchemaMixin(JSONSchemaModel):

    schema_base = {
        'title': 'todo list',
        'description': '',
        'type': 'object',
        'properties': {
            'id': {
                'type': 'integer',
            },
            'name': {
                'type': 'string',
            },
            'description': {
                'type': 'string',
            },
            'item_list': {
                'type': 'array',
                'items': TodoItemSchemaMixin.schema(),
            },
        },
    }

    def to_dict(self):
        name_list = ['id', 'name', 'description']
        response_dict = {x: getattr(self, x) for x in name_list}
        response_dict['item_list'] = [x.to_dict() for x in self.get_item_list()]
        return response_dict
