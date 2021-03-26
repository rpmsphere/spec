Name:           omnitux
Summary:        Educational activities around multimedia elements
Version:        1.2.0
Release:        1
Group:          Amusements/Teaching/Mathematics
License:        GPL, Creative Commons, Creative Commons Attribution-Noncommercial-Share Alike
URL:            http://omnitux.sourceforge.net/
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.svg
Patch1:         omnitux-new_from_file_at_size.patch
Requires:       pygame
Requires:       pygtk2

%description
The project aims to provide various educational activities around multimedia
elements (images, sounds, texts). Omnitux provides various different activity
types including associations, puzzles and counting. 

Authors:
-------
    Olav_2 : coding, creation of French and English activities
    Kot26 : Polish activities
    Manfred Schulenburg : German activities
    Iwan Gabovitch : German translation of this website

%prep
%setup -q -n %{name}
%patch1 -p0
find -iname "*.pyc" -delete

%build

%install
mkdir -p %buildroot%{_bindir}
mkdir -p %buildroot%{_datadir}/%{name}
mkdir -p %buildroot%{_defaultdocdir}/%{name}/
cp -a * %buildroot%{_datadir}/%{name}/
# cleanup
rm -rf %buildroot%{_datadir}/%{name}/log
# docu
for file in LICENSE.txt README.txt ; do
	mv %buildroot%{_datadir}/%{name}/$file %buildroot%{_defaultdocdir}/%{name}/
done
chmod +x %buildroot%{_datadir}/%{name}/*.sh
#
# install binfile
cat > %buildroot%{_bindir}/%{name} << EOF
#!/bin/bash
cd %{_datadir}/%{name}
/bin/bash omnitux.sh
EOF
chmod +x %buildroot%{_bindir}/%{name}
#
# below is the desktop file and icon stuff.
install -Dm 644 %SOURCE1 %buildroot%{_datadir}/applications/%{name}.desktop
install -Dm 644 %SOURCE2 %buildroot%{_datadir}/pixmaps/%{name}.svg
#
desktop-file-install \
  --dir=%buildroot/%_datadir/applications \
  %SOURCE1

%clean
rm -rf %buildroot

%files
%doc %{_defaultdocdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuild for Fedora
* Mon May 21 2012 johnwu<johnwu@ossii.com.tw>
- rebuild for OX
* Mon Sep 19 2011 lars@linux-schulserver.de
- update to 1.2.0
- remove pyc files with outdated mtime
- added omnitux-new_from_file_at_size.patch casting the
  desired_with and desired_heigh values to int (bnc #711902)
* Fri Sep 25 2009 lars@linux-schulserver.de
- update to 0.9.0:
* Mon Jun 15 2009 lars@linux-schulserver.de
- update to 0.8.0:
  + graphical improvements by Tutur
  + difficulty levels in some activities
  + new activity : 'animal sounds'
  + various bug fixes and clean up.
* Wed May 20 2009 lars@linux-schulserver.de
- initial version 0.7.1
