Name:	        oxpacker	
Version:	0.5
Release:	2
Summary:        media tools

Group:	        Development/Tools	
License:	Commercial
		
Source0:	%{name}-%{version}.tar.gz

#BuildRequires:	
Requires:	oxzilla, calibre, sigil, oxoffice, epub-tools, oxezip
BuildArch:      noarch


%description
This program is used to integrate media tools

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q


%install
rm -rf $RPM_BUILD_ROOT

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=OX packer
Name[zh_TW]=數位媒體工具
Icon=oxezip
Comment=ox document tools
Comment[zh_TW]=利用OXZilla編寫的多媒體工具整合
Categories=Application;Utility;
Exec=oxpacker
Terminal=false
Type=Application
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

%__mkdir_p ${RPM_BUILD_ROOT}%{_bindir}/

echo -e '#!/bin/sh\ncd %{_datadir}/%{name}\noxzilla -s 288x100 index.html;' > ${RPM_BUILD_ROOT}%{_bindir}/%{name}

chmod +x ${RPM_BUILD_ROOT}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_datadir}/%{name}/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Fri Jun 4 2010 Harry <harry@ossii.com.tw> 0.5-2
- Initial build
* Wed May 19 2010 Harry <harry@ossii.com.tw> 0.5-1
- Initial build
* Tue May 18 2010 Harry <harry@ossii.com.tw> 0.4-1
- Initial build
* Wed May 12 2010 Harry <harry@ossii.com.tw> 0.3-1
- Initial build
* Tue May 04 2010 Harry <harry@ossii.com.tw> 0.2-1
- Initial build
* Mon Apr 19 2010 Harry <harry@ossii.com.tw> 0.1-1
- Initial build
