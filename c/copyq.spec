Summary:	Advanced clipboard manager
Name:		copyq
Version:	2.0.0
Release:	6.1
License:	GPLv3
Group:		Accessibility
URL:		http://sourceforge.net/projects/copyq/
Source0:	http://sourceforge.net/projects/copyq/files/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ImageMagick
BuildRequires:	qt-devel
BuildRequires:	qtwebkit-devel

%description
CopyQ is advanced clipboard manager with searchable and editable history with
support for image formats, command line control and more.

Features:
- Supports Windows and Linux.
- Store text, HTML, images and any other custom format.
- Customize tray menu.
- Save items in new tabs.
- Quickly browse through items (fast navigation, filtering with matched text
  highlighting).
- Sort items, create new, remove, copy/paste to different tab.
- Variety of system-wide shortcuts (e.g. show main window or tray, edit
  clipboard, copy next/previous item, paste as plain text).
- Immediately paste to focused window from tray or main window.
- Fully customizable appearance (colors, fonts, transparency).
- Advanced command-line interface and scripting.
- Ignore clipboard copied from some windows or containing some text.
- Apply custom commands on selected items or automatically when new matching
  clipboard content is available.

%prep
%setup -q
sed -i s,"/lib/","/%{_lib}/",g CMakeLists.txt

%build
%cmake
make

%install
%make_install

%files
%doc AUTHORS LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.svg

%changelog
* Fri Jan 03 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.0
- Rebuilt for Fedora
