'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: dom_debugger
Experimental: False
'''

from dataclasses import dataclass, field
import typing

from .types import *
from ..dom import types as dom
from ..runtime import types as runtime



class DOMDebugger:
    @staticmethod
    def get_event_listeners(object_id: runtime.RemoteObjectId, depth: int, pierce: bool) -> typing.List['EventListener']:
        '''
        Returns event listeners of the given object.
        
        :param object_id: Identifier of the object to return listeners for.
        :param depth: The maximum depth at which Node children should be retrieved, defaults to 1. Use -1 for the
        entire subtree or provide an integer larger than 0.
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree
        (default is false). Reports listeners for all contexts if pierce is enabled.
        :returns: Array of relevant listeners.
        '''

        cmd_dict = {
            'method': 'DOMDebugger.getEventListeners',
            'params': {
                'objectId': object_id,
                'depth': depth,
                'pierce': pierce,
            }
        }
        response = yield cmd_dict
        return [EventListener.from_response(i) for i in response['listeners']]

    @staticmethod
    def remove_dom_breakpoint(node_id: dom.NodeId, type: DOMBreakpointType) -> None:
        '''
        Removes DOM breakpoint that was set using `setDOMBreakpoint`.
        
        :param node_id: Identifier of the node to remove breakpoint from.
        :param type: Type of the breakpoint to remove.
        '''

        cmd_dict = {
            'method': 'DOMDebugger.removeDOMBreakpoint',
            'params': {
                'nodeId': node_id,
                'type': type,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def remove_event_listener_breakpoint(event_name: str, target_name: str) -> None:
        '''
        Removes breakpoint on particular DOM event.
        
        :param event_name: Event name.
        :param target_name: EventTarget interface name.
        '''

        cmd_dict = {
            'method': 'DOMDebugger.removeEventListenerBreakpoint',
            'params': {
                'eventName': event_name,
                'targetName': target_name,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def remove_instrumentation_breakpoint(event_name: str) -> None:
        '''
        Removes breakpoint on particular native event.
        
        :param event_name: Instrumentation name to stop on.
        '''

        cmd_dict = {
            'method': 'DOMDebugger.removeInstrumentationBreakpoint',
            'params': {
                'eventName': event_name,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def remove_xhr_breakpoint(url: str) -> None:
        '''
        Removes breakpoint from XMLHttpRequest.
        
        :param url: Resource URL substring.
        '''

        cmd_dict = {
            'method': 'DOMDebugger.removeXHRBreakpoint',
            'params': {
                'url': url,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_dom_breakpoint(node_id: dom.NodeId, type: DOMBreakpointType) -> None:
        '''
        Sets breakpoint on particular operation with DOM.
        
        :param node_id: Identifier of the node to set breakpoint on.
        :param type: Type of the operation to stop upon.
        '''

        cmd_dict = {
            'method': 'DOMDebugger.setDOMBreakpoint',
            'params': {
                'nodeId': node_id,
                'type': type,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_event_listener_breakpoint(event_name: str, target_name: str) -> None:
        '''
        Sets breakpoint on particular DOM event.
        
        :param event_name: DOM Event name to stop on (any DOM event will do).
        :param target_name: EventTarget interface name to stop on. If equal to `"*"` or not provided, will stop on any
        EventTarget.
        '''

        cmd_dict = {
            'method': 'DOMDebugger.setEventListenerBreakpoint',
            'params': {
                'eventName': event_name,
                'targetName': target_name,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_instrumentation_breakpoint(event_name: str) -> None:
        '''
        Sets breakpoint on particular native event.
        
        :param event_name: Instrumentation name to stop on.
        '''

        cmd_dict = {
            'method': 'DOMDebugger.setInstrumentationBreakpoint',
            'params': {
                'eventName': event_name,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_xhr_breakpoint(url: str) -> None:
        '''
        Sets breakpoint on XMLHttpRequest.
        
        :param url: Resource URL substring. All XHRs having this substring in the URL will get stopped upon.
        '''

        cmd_dict = {
            'method': 'DOMDebugger.setXHRBreakpoint',
            'params': {
                'url': url,
            }
        }
        response = yield cmd_dict
