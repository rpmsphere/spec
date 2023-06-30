%undefine _debugsource_packages

Name:       amiwm
Version:	0.21pl2
Release:	22.1
Summary:	Amiga Window Manager
Group:		System/GUI/Other
License:	Generic
URL:		https://www.lysator.liu.se/~marcus/amiwm.html
Source:		ftp://ftp.lysator.liu.se/pub/X11/wm/amiwm/amiwm0.21pl2.tar.gz
Patch0:        amiwm-includes.diff
BuildRequires: libX11-devel
BuildRequires: libXmu-devel
BuildRequires: bison flex

%description
amiwm is an X window manager that tries to make your display look and feel
like an Amiga® Workbench® screen. It is fully functional and can do all the
usual window manager stuff, like moving and resizing windows.

The purpose of amiwm is to make life more pleasant for Amiga-freaks like
myself who has/wants to use UNIX workstations once in a while. It can also
be used on the Amiga with the AmiWin X server, although this part needs some
more work.

Authors:
--------
    Marcus Comstedt (marcus@mc.pp.se) 

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

%build
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --exec_prefix=%{_exec_prefix}
make %{?_smp_flags} prefix=%{_prefix} exec_prefix=%{_prefix} bindir=%{_bindir} libdir=%{_libdir} mandir=%{_mandir}

%install
%makeinstall prefix=%{buildroot}%{_prefix} exec_prefix=%{buildroot}%{_prefix} bindir=%{buildroot}%{_bindir} libdir=%{buildroot}%{_libdir} mandir=%{buildroot}%{_mandir}
rm %{buildroot}%{_bindir}/requestchoice
ln -s ../%{_lib}/amiwm/requestchoice %{buildroot}%{_bindir}/requestchoice
sed -i s!%{buildroot}!! %{buildroot}%{_libdir}/amiwm/Xinitrc
sed -i s!%{buildroot}!! %{buildroot}%{_libdir}/amiwm/Xsession
sed -i s!%{buildroot}!! %{buildroot}%{_libdir}/amiwm/Xsession2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README README.modules LICENSE
%{_bindir}/amiwm
%{_bindir}/ppmtoinfo
%{_bindir}/requestchoice
%{_libdir}/amiwm
%{_mandir}/man1/amiwm.1.*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.21pl2
- Rebuilt for Fedora
* Wed Feb 27 2013 wbauer@tmo.at
- fix build on 12.3
* Sat Dec 04 2010 wbauer@tmo.at
- initial package
