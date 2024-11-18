%undefine _debugsource_packages

Summary:        Multiseat Display Manager
Name:           multiseat
Version:        0.0.3
Release:        1
License:        GPLv2
Group:          User Interface/X
URL:            https://github.com/anderco/mdm
Source0:        mdm-%{version}.tar.gz
BuildRequires:  libXft-devel, libX11-devel, cairo-devel, freetype-devel
Requires:       gdm, xorg-x11-server-Xephyr

%description
A manager that makes the computer a multiseat computer. Despite its name,
mdm is actually a wrapper on the real display manager. It is used to configure
multiseat environments, allowing users to change a normal machine into a
multiseat machine by just installing a package.

%prep
%setup -q -n mdm-%{version}
for i in mdm/po/*.po ; do
sed -i '1i msgid ""\nmsgstr ""\n"Content-Type: text/plain; charset=UTF-8"' $i
done

%build
make
make -C extra-modes/xephyr-gdm

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install -C extra-modes/xephyr-gdm
sed -i "s|$RPM_BUILD_ROOT|/|" $RPM_BUILD_ROOT/usr/sbin/*

%files
%doc AUTHORS COPYING MAINTAINERS README TODO
%{_sysconfdir}/gdm/gdm.conf
%{_sysconfdir}/gdm/gdm.conf-custom
%{_sysconfdir}/init.d/mdm
%{_sysconfdir}/mdm
%{_sbindir}/*
%{_datadir}/locale/*/LC_MESSAGES/mdm.mo
%{_datadir}/mdm

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.3
- Rebuilt for Fedora
