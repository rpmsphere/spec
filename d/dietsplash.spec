Summary:	Simple bootsplash
Name:		dietsplash
Version:	0.3
Release:	7.1
License: 	GPLv3
Group: 		Applications/System
Source:		http://git.profusion.mobi/cgit.cgi/lucas/dietsplash/snapshot/%{name}-%{version}.tar.bz2
URL:		http://git.profusion.mobi/cgit.cgi/lucas/dietsplash/
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Simple bootsplash that aims to adhere to the KISS philosophy. It's possible to
put a background and simple animations are on the way to be supported. Since
bootsplashes are most likely to be done by distro maintainers and are not
meant to be easily changed by user, dietsplash is developed without scripting
and lots of configurations like others. Its configurations are almost all done
during compile time, including custom animations.

That said, dietsplash is targeted as a small bootsplash to be used in embedded
systems but that can also be used on desktop. We keep it small and with not
extra dependencies so all our precious I/O time can be used to actually boot
faster.

%prep
%setup -q

%build
%configure
make

%install
rm -fr $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README
/bin/%{name}
%{_bindir}/%{name}ctl
%if 0%{fedora} > 16
/usr/lib/systemd/system/*
%else
/lib/systemd/system/*
%endif

%changelog
* Sun Oct 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
