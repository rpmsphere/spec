Summary: 	Testing theme for the Matchbox Desktop
Name: 		matchbox-tests
Version: 	0.4
Release: 	1
URL: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
Testing theme for the panel from Matchbox.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING ChangeLog
%_datadir/themes/mbtest


%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Tue Feb 01 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- initial package
