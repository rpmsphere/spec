%if "%{_target_cpu}" == "ppc"
   %define model powerbook
%else
   %define model i386
%endif

Name:          pbbuttonsd
Version:       0.8.1a
Release:       9.1
Summary:       Support for Laptops special functions
Group:         System/Servers
URL:           https://pbbuttons.berlios.de/projects/pbbuttonsd/
Source:        https://switch.dl.sourceforge.net/sourceforge/pbbuttons/pbbuttonsd-%{version}.tar.gz
Source1:       %{name}.init
License:       GPL
BuildRequires: glib2-devel
BuildRequires: gcc-c++

%description
PBButtons is a program suite to support laptop specific functions and make them 
available again under Linux.
Basically it was developed to support the special hotkeys of an Apple iBook, 
Powerbook or TiBook but since version 0.5 the design has been changed to 
support all kind of laptops or notebooks.

With this programms the keys for the display brightness, the volume of speaker 
and headphone, the mute key and the eject key will do their job as expected.
The daemon also do some power management tasks including low battery warnings, 
dimming the display if idle, sleep on command, etc.

The main part of PBButtons is the daemon pbbuttonsd which work as a server that 
do all the work.
It runs in background and is preferable started at boot time.
Multiple clients could register themselves to get messages about events from 
the server.

The smallest client is pbbcmd which allows to change all of pbbuttonsd options 
at runtime from the command line.
It could ask for the status of each option and could also change it.
This client is now part of the pbbuttonsd package.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{?epoch:%epoch:}%{version}

%description devel
PBButtons is a program suite to support laptop specific functions and make them 
available again under Linux.
Basically it was developed to support the special hotkeys of an Apple iBook, 
Powerbook or TiBook but since version 0.5 the design has been changed to 
support all kind of laptops or notebooks.

With this programms the keys for the display brightness, the volume of speaker 
and headphone, the mute key and the eject key will do their job as expected.
The daemon also do some power management tasks including low battery warnings, 
dimming the display if idle, sleep on command, etc.

The main part of PBButtons is the daemon pbbuttonsd which work as a server that 
do all the work.
It runs in background and is preferable started at boot time.
Multiple clients could register themselves to get messages about events from 
the server.

The smallest client is pbbcmd which allows to change all of pbbuttonsd options 
at runtime from the command line.
It could ask for the status of each option and could also change it.
This client is now part of the pbbuttonsd package.

This package contains static libraries and header files need for development.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure LAPTOP=%{model}
make CFLAGS+=-Wno-format-security

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
install -D -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/%{name}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# new install
mv  %{_sysconfdir}/%{name}.conf  %{_sysconfdir}/%{name}.cnf
if [ $1 -eq 1 ]; then
   /sbin/chkconfig --add %{name}
   service %{name} start
fi
:

%preun
# erase
if [ $1 -eq 0 ]; then
   service %{name} stop
   /sbin/chkconfig --del %{name}
fi
:

%postun
# upgrade
if [ $1 -eq 1 ]; then
   /sbin/chkconfig %{name}
   [ $? -eq 0 ] && service %{name} restart
fi
:

%files -f %{name}.lang
%{_bindir}/pbbcmd
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.cnf
%config(noreplace) %{_sysconfdir}/power/README
%config(noreplace) %{_sysconfdir}/power/pmcs*
%config(noreplace) %{_sysconfdir}/power/event.d/*
%config(noreplace) %{_sysconfdir}/power/scripts.d/*
%config(noreplace) %{_initrddir}/%{name}
%dir %{_localstatedir}/lib/ibam
%{_mandir}/man1/*
%{_mandir}/man5/*
%doc AUTHORS BUGS COPYING ChangeLog README TODO

%files devel
%{_includedir}/*.h
%{_libdir}/libpbb.a

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.1a
- Rebuilt for Fedora
* Fri Feb 05 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 0.8.1a-2mamba
- rebuilt to remove executable requirements
* Tue May 13 2008 Tiziana Ferro <tiziana.ferro@email.it> 0.8.1a-1mamba
- update to 0.8.1a
* Wed May 17 2006 Stefano Cotta Ramusino <stefano.cotta@qilinux.it> 0.7.5-1qilnx
- package created by autospec
