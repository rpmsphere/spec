%undefine _missing_build_ids_terminate_build

Summary: Penpower Handwriting Writepanel
Name: hwr_writepanel
Version: 0.1demo
Release: 1%{?dist}.bin
License: Commercial
Group: System/Internationalization
Source: hwr_writepanel_0.1.tar.gz
Source1: penpower.png
URL: http://www.penpower.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: gtk2

%description
Penpower handwriting recognition solutions with writepanel.

%prep
%setup -q -n "hwr_writepanel/writepanal_ap/Write Panel"

%build
%install
rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -R %{SOURCE1} * %{buildroot}%{_datadir}/%{name}

%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_datadir}/%{name}/src
if ps -C pphwrwp ; then
  pkill -9 pphwrwp
else
  ./pphwrwp
fi
EOF

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Writepanel
Name[zh_TW]=手寫輸入
Comment=Penpower Handwriting Writepanel
Comment[zh_TW]=蒙恬手寫輸入板
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/penpower.png
Categories=Application;Utility;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Feb 18 2009 Wei-Lun Chao <bluebat@member.fsf.org> 0.1demo-1.ossii
- Initial package

