Name:           gtk-experience-engine
Version:        0.10.5
Release:        1.1
Summary:        GTK engine for eXperience theme
Group:          System Environment/Libraries
License:        LGPL
URL:            http://benjamin.sipsolutions.net/Projects/eXperience
Source0:        http://benjamin.sipsolutions.net/experience/gtk-engine-experience-%{version}.tar.gz
BuildRequires:  gtk2-devel
Requires:       gtk2

%description
Benjamin Berg created the eXperience-GTK engine as a project
to help his brother with the Luna style GTK-Theme.

%prep
%setup -q -n gtk-engine-experience-%{version}

%build
%configure
sed -i 's|-Wall|-Wall -Wl,--allow-multiple-definition|' Makefile */Makefile
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc TODO README COPYING NEWS ChangeLog AUTHORS
%{_libdir}/gtk-2.0/*/engines/*

%changelog
* Sun Mar 03 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.10.5
- Rebuild for Fedora
