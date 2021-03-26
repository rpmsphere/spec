Name:		oxezip
Version:	0.5
Release:	7
Summary:	Open ezip by html and javascript.
Group:		Amusements/Eduactions
License:	Commercial
URL:		http://www.ossii.com.tw/
Source0:	%{name}.tar.gz
Source1:	%{name}.xml
Source2:	%{name}.png
BuildArch:	noarch
Requires:	oxzilla, oxzilla-jscollections, fuse, fuse-zip, oxquiz, oxular, oxepubview, evince, epdfview, calibre, fbreader, ffmpeg, gnash, gnash-plugin, zenity

%description
Open ezip by html and javascript.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/
cd $RPM_BUILD_ROOT%{_datadir}/
tar zxvf %{SOURCE0} 
cd -

# Mime type
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime/packages/
%__cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mime/packages/

# Mime png
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
%__cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/

# Bin
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat >$RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
export ezip_PWD="\$PWD"
export ezip_path="\$1"
cd %{_datadir}/%{name}
oxzsh index.html
EOF

# Desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=OX Ezip
Name[zh_TW]=OX Ezip 閱讀器
Comment=OXezip written in OXZilla
Comment[zh_TW]=利用 OXZilla 編寫的閱讀器
Categories=Application;Education;
Exec=%{name}
Terminal=false
Type=Application
MimeType=application/x-ezip;
Hidden=false
NoDisplay=true
EOF

%post
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,root,root,0755)
%{_datadir}/%{name}/index.html
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Thu Jul 29 2010 Kami <kami@ossii.com.tw> 0.5-7.ossii
- oxezip can open new ezip format

* Mon Jul 5 2010 Kami <kami@ossii.com.tw> 0.5-6.ossii
- oxezip change own picture for its format

* Fri Jun 25 2010 Kami <kami@ossii.com.tw> 0.5-5.ossii
- oxezip has own picture for its format

* Mon Jun 21 2010 Kami <kami@ossii.com.tw> 0.5-4.ossii
- oxezip use oxzsh to open

* Tue Jun 15 2010 Kami <kami@ossii.com.tw> 0.5-3.ossii
- oxezip can use not only one reader if the first can't work
- oxezip page to be hidden

* Mon May 27 2010 Kami <kami@ossii.com.tw> 0.5-2.ossii
- oxezip can read both absolute path and relative path
- use mktemp directory to store ezip files

* Mon May 24 2010 Kami <kami@ossii.com.tw> 0.5-1.ossii
- Build for OSSII
