Name: osso-af-settings
License: GPL
Group: User Interface/Desktops
Summary: pkg-config settings for Maemo/OS 2006.
Version: 0.9.1
Release: 2
Source: osso-af-settings_0.9.1-2.tar.gz
BuildArch: noarch

%description
pkg-config settings for Maemo/OS 2006.


%prep
%setup -q -n osso-af-settings

%build
%configure
%__make

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root)
%{_libdir}/pkgconfig/osso-af-settings.pc

%changelog
* Tue Jun 3 2008 Wei-Lun Chao <bluebat@member.fsf.org> 0.9.1-2.ossii
- Initial package
