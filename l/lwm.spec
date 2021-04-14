%undefine _debugsource_packages

Name:           lwm
Version:        1.2.4
Release:        4.1
Summary:        Lightweight Window Manager
Group:          User Interface/X
License:        GPLv2
URL:            http://www.jfc.org.uk/software/lwm.html
Source0:        http://www.jfc.org.uk/files/lwm/%{name}-%{version}.tar.gz
Source1:        lwm.desktop
BuildRequires:  imake, libXext-devel, libSM-devel
Requires:       xterm
Patch0:         lwm-1.2.4.git.patch

%description
lwm is a window manager for X that tries to keep out of your face.
There are no icons, no button bars, no icon docks, no root menus, no nothing:
if you want all that, then other programs can provide it.
There's no configurability either: if you want that, you want
a different window manager; one that helps your operating system in its evil
conquest of your disc space and its annexation of your physical memory.

%prep
%setup -q
%patch0 -p1

%build
xmkmf
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 lwm $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 0644 lwm.man $RPM_BUILD_ROOT%{_mandir}/man1/lwm.1
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xsessions
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/lwm.desktop

%files
%doc AUTHORS COPYING TODO README ChangeLog BUGS
%{_bindir}/lwm
%{_mandir}/man1/lwm.1.*
%{_datadir}/xsessions/lwm.desktop

%changelog
* Tue Mar 29 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.4
- Rebuilt for Fedora
* Thu Apr 05 2012 Damien Durand <splinux25@gmail.com> - 1.2.2-1
- Initial release.
