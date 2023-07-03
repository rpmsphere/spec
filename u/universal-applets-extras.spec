%define __python /usr/bin/python2
Name:          universal-applets-extras
Version:       0.1bzr172
Release:       1
License:       GPL
URL:           https://www.screenlets.org/index.php/Home
Summary:       OsX Like Dashboard
Group:         System/X11/Utilities
# to get the newest source use
# bzr co lp:~universal-applets-extras-team/universal-applets/universal-applets-extras
Source:        universal-applets-extras_0.1bzr172-1.tar.gz
BuildRequires: python2-devel
BuildArch:     noarch
Requires:      universal-applets
Obsoletes:     screenlets
Obsoletes:     3rd-party-screenlets
Obsoletes:     screenlets-extras

%description
Screenlets are small owner-drawn applications (written in Python)
that can be described as 'the virtual representation of things 
lying/standing around on your desk'. Sticknotes, clocks, rulers, ...
the possibilities are endless.
You do NOT need Compiz or Beryl to use screenlets

%prep
%setup -q -n uae-bzr

# %build
# %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --prefix /usr

sed -i -e 's|/usr/bin/python$|/usr/bin/python2|' -e 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{_datadir}/screenlets/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/screenlets/*
/usr/lib*/python*/site-packages/universal_applets_extras*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1bzr172
- Rebuilt for Fedora
* Tue Mar 03 2009 - Ketil Wendelbo Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Mon Mar 02 2009 - some-guy <muhammedu@gmail.com>
- upgraded to bzr
* Mon Mar 02 2009 - some-guy <muhammedu@gmail.com>
- upgraded to bzr
* Mon Mar 02 2009 - some-guy <muhammedu@gmail.com>
- upgraded to bzr
* Mon Mar 02 2009 - some-guy <muhammedu@gmail.com>
- upgraded to bzr
* Sun Feb 22 2009 - Ketil Wendelbo Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Tue Jan 06 2009 - Ketil Wendelbo Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Fri Jan 02 2009 - Ketil Wendelbo Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Fri Jan 02 2009 - Ketil Wendelbo Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Fri Jan 02 2009 - Ketil Wendelbo Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Mon Dec 29 2008 - Ketil Wendelbo Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Fri Dec 19 2008 - Ketil W. Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Tue Dec 16 2008 - Ketil W. Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Sat Dec 06 2008 - Ketil W. Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Tue Dec 02 2008 - Ketil W. Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Mon Dec 01 2008 - Ketil W. Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Fri Nov 28 2008 - Ketil W. Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Fri Nov 28 2008 - Ketil W. Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
