Summary: Library screen
Name: oxlibrary
Version: 0.3
Release: 1
License: Commercial
Group: Applications/Multimedia
Source0: library.tar.gz
Source1: library_book.png
Source2: library_exam.png
Requires: oxzilla, oxzilla-gio, oxzilla-devel, oxzilla-mysql, oxzilla-jscollections, oxquiz, oxezip, oxular, oxepubview, evince, epdfview, calibre, fbreader, ffmpeg, gnash, gnash-plugin, zenity
BuildArch: noarch

%description
Library screen using OXZilla.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/
cd $RPM_BUILD_ROOT%{_datadir}/
tar zxf %{SOURCE0}
cd -

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
%__cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/
%__cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat >$RPM_BUILD_ROOT%{_bindir}/oxbooks <<EOF

#!/bin/bash
cd %{_datadir}/library
oxzilla -s 600x600 books.html?Divergence=3
EOF
%__cat >$RPM_BUILD_ROOT%{_bindir}/oxexams <<EOF
#!/bin/bash
cd %{_datadir}/library
oxzilla -s 600x600 books.html?Divergence=4
EOF


#Desktop
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%{__cat} > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}_books.desktop << EOF
[Desktop Entry]
Name=OX Library
Name[zh_TW]=OX 圖書庫
Comment=Library written in OXZilla
Comment[zh_TW]=利用 OXZilla 編寫的圖書庫
Icon=library_book.png
Exec=oxbooks
Terminal=false
Type=Application
Categories=Application;Education;
Encoding=UTF-8
EOF

%{__cat} > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}_exam.desktop << EOF
[Desktop Entry]
Name=OX Library
Name[zh_TW]=OX 試卷庫
Comment=Library written in OXZilla
Comment[zh_TW]=利用 OXZilla 編寫的試卷庫
Icon=library_exam.png
Exec=oxexams
Terminal=false
Type=Application
Categories=Application;Education;
Encoding=UTF-8
EOF

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0777,root,root,0777)
%{_datadir}/library
%{_datadir}/pixmaps/library_book.png
%{_datadir}/pixmaps/library_exam.png
%{_datadir}/applications/%{name}_exam.desktop
%{_datadir}/applications/%{name}_books.desktop
%{_bindir}/oxbooks
%{_bindir}/oxexams

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Thu Dec 23 2010 Sean <sean@ossii.com.tw> 0.3-1
- Add Auto detect New ezip File and write to databese
- Modify .desktop setting.
- Modify UI width & height

* Wed Jul 7 2010 Kami <kami@ossii.com.tw> 0.2-6
- Modify ebook shelf be able to up and down.
- Modify etest cover.

* Fri Jul 2 2010 Kami <kami@ossii.com.tw> 0.2-5
- Modify ebook open by using oxezip.
- Modify etest import data and turns.
- Modify UI width be able to resize.

* Fri Jun 25 2010 Kami <kami@ossii.com.tw> 0.2-4
- Implement ebook Add option.
- Implement ebook Modify option.
- Implement ebook Delete option.

* Wed Jun 2 2010 Kami <kami@ossii.com.tw> 0.2-3
- Modify ebook reader option.

* Wed Jun 2 2010 Kami <kami@ossii.com.tw> 0.2-2
- Modify ebook Requires.

* Wed Jun 2 2010 Kami <kami@ossii.com.tw> 0.2-1
- Implement ebook Requires.
- Implement ebook alert message.

* Wed Jun 2 2010 Kami <kami@ossii.com.tw> 0.1-16
- Implement ebook reader option.

* Thu May 13 2010 Kami <kami@ossii.com.tw> 0.1-15
- Upload ebook modified.
- Delete ebook updated.

* Tue Mar 30 2010 Kami <kami@ossii.com.tw> 0.1-14
- Update ebook database.

* Fri Mar 05 2010 Kami <kami@ossii.com.tw> 0.1-13
- Open ebook fixed.

* Thu Mar 04 2010 Kami <kami@ossii.com.tw> 0.1-12
- OXZilla plugins replaced.

* Mon Feb 23 2010 Kami <kami@ossii.com.tw> 0.1-11
- Implement File selector.

* Mon Feb 22 2010 Kami <kami@ossii.com.tw> 0.1-10
- Library theme updated.

* Fri Feb 12 2010 Kami <kami@ossii.com.tw> 0.1-9
- Function Upload updated.

* Wed Feb 05 2010 Kami <kami@ossii.com.tw> 0.1-8
- Change content of .desktop file.

* Wed Feb 03 2010 Kami <kami@ossii.com.tw> 0.1-7
- Modify or OXZilla compatibility.

* Mon Feb 01 2010 Kami <kami@ossii.com.tw> 0.1-6
- Modify for License.

* Fri Jan 15 2010 Kami <kami@ossii.com.tw> 0.1-5
- Modify problem of base64_decode cover image.

* Wed Jan 13 2010 Kami <kami@ossii.com.tw> 0.1-4
- Implement exam page to browse and execute.

* Tue Jan 05 2010 Kami <kami@ossii.com.tw> 0.1-3
- Implement *.xol data format be able to read.

* Fri Dec 25 2009 Kami <kami@ossii.com.tw> 0.1-2
- Implement function for upload ezip to database.

* Fri Dec 11 2009 Kami <kami@ossii.com.tw> 0.1-1
- Building on first time.
