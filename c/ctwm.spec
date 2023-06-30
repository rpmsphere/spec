%undefine _debugsource_packages

Summary:       Claude's Tab Window Manager
Name:          ctwm
Version:       4.0.3
Release:       1
BuildRequires: libX11-devel libjpeg-devel libXt-devel libXext-devel libXmu-devel libXpm-devel
BuildRequires: cmake
Source0:       https://www.ctwm.org/dist/%{name}-%{version}.tar.gz
Source1:       %{name}.desktop
License:       MIT
Group:         User Interface/X
URL:           https://www.ctwm.org/
Requires:      m4

%description
Ctwm is a window manager for the X Window System.  It provides
titlebars, shaped windows, virtual screens (workspaces), several forms
of icon management, user-defined macro functions, click-to-type and
pointer-driven keyboard focus, and user-specified key and pointer
button bindings.  It is actually twm (Tab Window Manager) from the MIT
X11 distribution slightly modified to accommodate the use of several
virtual screens (workspaces). It is heavily inspired from the
Hewlett-Packard vuewm window manager.  In addition, ctwm can use
coloured, shaped icons and background root pixmaps in XPM and JPG format,
as well as any format understood by the imconv package [from the
San Diego Supercomputer Center] and xwd files.  Ctwm can be compiled
to use both, either or none of the above icon/pixmap formats.

%prep
%setup -q

%build
#cd build
%cmake
%cmake_build

%install
%cmake_install
%{__install} -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.md CHANGES.md COPYRIGHT
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_datadir}/xsessions/%{name}.desktop
%{_datadir}/ctwm
%{_datadir}/doc/ctwm/ctwm.1.html
%{_datadir}/examples/ctwm/system.ctwmrc

%changelog
* Tue Dec 24 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.3
- Rebuilt for Fedora
* Sat Apr  9 2011 Agnelo de la Crotche <agnelo@unixversal.com>
- package for openSUSE 11.3/11.4
* Thu Feb 16 2006 Richard Levitte <richard@levitte.org>
- Release ctwm 3.8a.
* Wed May  4 2005 Rudolph T Maceyko <rm55@pobox.com>
- Tweaks.  Added all .ctwmrc files as well as sound and VMS docs.
* Wed May  4 2005 Richard Levitte <richard@levitte.org>
- Changed some directory specifications to RedHat-ish standards.
* Tue May  3 2005 Richard Levitte <richard@levitte.org>
- Received the original from Johan Vromans. Adjusted it to become
  an official .spec file.
