Summary:   Touch screen keyboard
Name:      oxim-touchboard
Version:   0.0.5
Release:   1
License:   GPL
Group:     System/Internationalization
Source0:   %{name}-%{version}.tar.gz  
BuildArch: noarch
Requires:  oxim

%description
Touch screen keyboard input for OXIM framework. 

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp phonetab.txt $RPM_BUILD_ROOT%{_datadir}/%{name}
cp %{name}  $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_bindir}

%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
cd /usr/share/%{name}
./%{name}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Mon May 10 2010 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.5-1
- Minor tweaks

* Tue Apr 28 2010 Gene <gene@ossii.com.tw> - 0.0.3-1
- Build for OSSII
