%define _name iAppliance3

Name:		iappliance3
Version:	0.1
Release:	3%{?dist}.bin
Summary:	iAppliance3 for Carbon Project
License:	GPL
Group:		System Environment/Utilities
Source:		%{_name}.tar.gz
Source1:	%{name}.desktop
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
#Requires:       adobeair1.0, adobe-certs

%description
iAppliance3 UI for Foxconn Carbon Project.

%prep
%setup -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT                
mkdir -p $RPM_BUILD_ROOT/opt
tar -zxvf %{SOURCE0} --directory=$RPM_BUILD_ROOT/opt/
%__install -D -m 644 %{SOURCE1} %{buildroot}/etc/xdg/autostart/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) /opt/*
%attr(755,root,root) /etc/xdg/autostart/*

%changelog
* Tue Sep 15 2009 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1-3
- Rebuild for OX1.5

* Sun Mar 08 2009 Victor Horng <victor@ossii.com.tw>
- Initial package for OX1
