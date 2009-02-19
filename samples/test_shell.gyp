{
  'variables': {
    'depth': '../../..',
  },
  'includes': [
    '../../../build/common.gypi',
  ],
  'targets': [
    {
      'target_name': 'test_shell',
      'type': 'executable',
      'sources': [
        'mac/DumpRenderTreePasteboard.h',
        'mac/DumpRenderTreePasteboard.m',
        'mac/KeystoneGlue.h',
        'mac/KeystoneGlue.m',
        'mac/test_shell_webview.h',
        'mac/test_shell_webview.mm',
        'mac/test_webview_delegate.mm',
        'mac/webview_host.mm',
        'mac/webwidget_host.mm',
        'drag_delegate.cc',
        'drag_delegate.h',
        'drop_delegate.cc',
        'drop_delegate.h',
        'event_sending_controller.cc',
        'event_sending_controller.h',
        'foreground_helper.h',
        'layout_test_controller.cc',
        'layout_test_controller.h',
        'resource.h',
        'simple_resource_loader_bridge.cc',
        'simple_resource_loader_bridge.h',
        'test_navigation_controller.cc',
        'test_navigation_controller.h',
        'test_shell.cc',
        'test_shell.h',
        'test_shell_gtk.cc',
        'test_shell_mac.mm',
        'test_shell_main.cc',
        'test_shell_platform_delegate.h',
        'test_shell_platform_delegate_gtk.cc',
        'test_shell_platform_delegate_mac.mm',
        'test_shell_platform_delegate_win.cc',
        'test_shell_request_context.cc',
        'test_shell_request_context.h',
        'test_shell_switches.cc',
        'test_shell_switches.h',
        'test_shell_win.cc',
        'test_webview_delegate.cc',
        'test_webview_delegate.h',
        'test_webview_delegate_gtk.cc',
        'test_webview_delegate_win.cc',
        'text_input_controller.cc',
        'text_input_controller.h',
        'webview_host.h',
        'webview_host_gtk.cc',
        'webview_host_win.cc',
        'webwidget_host.h',
        'webwidget_host_gtk.cc',
        'webwidget_host_win.cc',
      ],
      'include_dirs': [
        '../../..',
      ],
      'dependencies': [ 
        '../../webkit.gyp:glue',
        '../../../base/base.gyp:base',
        '../../../base/base.gyp:base_gfx',
        '../../../testing/gtest.gyp:gtest',
        '../../../skia/skia.gyp:skia',
        '../../../third_party/npapi/npapi.gyp:npapi',
      ],
      'conditions': [
        ['OS!="linux"', {'sources/': [['exclude', '_gtk\\.cc$']]}],
        ['OS!="mac"', {
          'sources/': [
            ['exclude', 'mac/[^/]*\\.(cc|mm?)$'],
            ['exclude', '_mac\\.(cc|mm?)$'],
          ]
        }],
        ['OS!="win"', {
          'sources/': [
            ['exclude', '_win\\.cc$']
          ],
          'sources!': [
            'drag_delegate.cc',
            'drop_delegate.cc',
          ],
        }],
      ],
    },
  ],
}