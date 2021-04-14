Name:           domterm
Version:        1.0
Release:        3.1
Summary:        A terminal emulator based on web technologies
License:        BSD1
URL:            https://domterm.org/
Source0: https://github.com/PerBothner/DomTerm/releases/download/domterm-%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(libwebsockets)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(openssl)
BuildRequires: ruby
BuildRequires: asciidoctor
BuildRequires: gcc
BuildRequires: gcc-c++
#BuildRequires: java-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtwebchannel-devel
BuildRequires: qt5-qtwebengine-devel

%description
A terminal emulator based on web technologies.
You can "print" images, tables, and other HTML forms.
Supports 24-bit color; xterm mouse events; solid xterm emulation.
Good handling of Unicode, CJK wide characters, and IME support.
Experimental builtin pager (like simplified 'less').
Builtin basic input line editor with history.
Styling using CSS.
Hide/show a command's output.

%package -n qtdomterm
Summary:        A terminal emulator using Qt and web technologies
License:        GPLv2+

%description -n qtdomterm
A terminal emulator using Qt and web technologies.

%prep
%autosetup -n domterm-%{version}
sed -i '1i #include <QWebEngineCertificateError>' qtdomterm/webview.cpp

%build
autoreconf
%configure --with-qtwebengine --with-libwebsockets
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/domterm.desktop %{buildroot}%{_datadir}/applications/qtdomterm.desktop

%files
%dir %{_datadir}/domterm
%dir %{_datadir}/domterm/electron
%dir %{_datadir}/domterm/help
%{_bindir}/domterm
%{_datadir}/domterm/domterm.jar
%{_datadir}/domterm/electron/main.js
%{_datadir}/domterm/electron/package.json
%{_datadir}/domterm/help/domterm-attach.html
%{_datadir}/domterm/help/domterm-attach.txt
%{_datadir}/domterm/help/domterm-browse.html
%{_datadir}/domterm/help/domterm-browse.txt
%{_datadir}/domterm/help/domterm-hcat.html
%{_datadir}/domterm/help/domterm-hcat.txt
%{_datadir}/domterm/help/domterm.html
%{_datadir}/domterm/help/domterm-imgcat.html
%{_datadir}/domterm/help/domterm-imgcat.txt
%{_datadir}/domterm/help/domterm-is-domterm.html
%{_datadir}/domterm/help/domterm-is-domterm.txt
%{_datadir}/domterm/help/domterm-list.html
%{_datadir}/domterm/help/domterm-list.txt
%{_datadir}/domterm/help/domterm-new.html
%{_datadir}/domterm/help/domterm-new.txt
%{_datadir}/domterm/help/domterm.txt
%{_datadir}/domterm/help/domterm-window-specifier.html
%{_datadir}/domterm/help/domterm-window-specifier.txt
%{_datadir}/applications/domterm.desktop
%{_datadir}/appdata/domterm.appdata.xml
%{_mandir}/man1/domterm.1*
%license COPYING

%files -n qtdomterm
%{_bindir}/qtdomterm
%{_mandir}/man1/qtdomterm.1*
%{_datadir}/applications/qtdomterm.desktop
%{_datadir}/appdata/qtdomterm.appdata.xml
%{_datadir}/domterm/help/qtdomterm.html
%{_datadir}/domterm/help/qtdomterm.txt
%license COPYING

%changelog
* Wed Jul 04 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Mon Mar 26 2018 Per Bothner <per@bothner.com> - 1.0-1
- Update for DomTerm 1.0
* Thu Mar 15 2018 Per Bothner <per@bothner.com> - 0.99-1
- Update for DomTerm 0.99.
* Mon Feb 12 2018 Per Bothner <per@bothner.com> - 0.96-1
- Update.
* Sat Apr  8 2017 Per Bothner <per@bothner.com> - 0.74-1
- Initial version.
