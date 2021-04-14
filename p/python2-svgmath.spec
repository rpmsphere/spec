Summary:    MathML-to-SVG converter
Name:       python2-svgmath
Version:    0.3.3
Release:    9.1
License:    MIT
Source0:    SVGMath-%{version}.tar.bz2
Source1:    svgmath.xml.in
Patch0:     math2svg.py.patch
Group:      Productivity/Graphics/Convertors
BuildRequires: python2-devel dos2unix
URL:        http://sourceforge.net/projects/svgmath/
BuildArch: noarch
%define fontdir     /usr/share/fonts/

%description
Converter from MathML (Mathematical Markup Language) to
SVG (Scalable Vector Graphics).

%prep
%define configfile svgmath.xml
%setup -q -n SVGMath-%{version}
%patch0
# Fix execution bit
for i in LICENSE.txt PKG-INFO README*; do
 [ -e "$i" ] && %{__chmod} -x "$i"
done

#[ -e LICENSE.txt ] && %{__chmod} -x LICENSE.txt
#[ -e PKG-INFO ] && %{__chmod} -x PKG-INFO
#[ -e README* ] && %{__chmod} -x README*

# Set permissions
for i in doc/* ; do
 %{__chmod} -x $i
 dos2unix $i
done
for i in svgmath/*.py ; do
  %{__chmod} -x $i
done

dos2unix math2svg.py
dos2unix svgmath.xml
dos2unix fo/adjustbase.xsl

%{__cat} %{S:1} | sed 's_@FONTPATH@_%{fontdir}_g' > %{configfile}
# mkdir examples && cp %{S:10} %{S:11} %{S:12} %{S:13} examples/.
%{__chmod} -x %{configfile} fo/adjustbase.xsl

%build
python2 setup.py build
dos2unix svgmath.xml

%install
python2 setup.py install \
  --root=$RPM_BUILD_ROOT \
  --prefix=%{_prefix}
%{__install} -m 755 -d $RPM_BUILD_ROOT%{_prefix}/bin/
%{__install} -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
%{__install} -m 755 math2svg.py $RPM_BUILD_ROOT%{_bindir}/math2svg
%{__install} -m 644 %{configfile} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{python2_sitelib}/svgmath
%{python2_sitelib}/SVGMath-*-info
%dir %{_sysconfdir}/%{name}/
%config %{_sysconfdir}/%name/*
%doc doc fo svgmath.xml
%{_bindir}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.3
- Rebuilt for Fedora
* Wed Sep 29 2010 toms@suse.de
- Used --record instead of only --record
- Disabled %%{py_sitedir} macro
  Fri May 29 09:05:00 CET 2009 - toms AT suse.de
  Corrected minor SPEC file issues and corrected build error
  Sat Feb 07 22:26:00 CEST 2009 - toms AT suse.de
- Update 0.3.3:
  Bugfixing release: AFM processing repaired
- svgmath.changes -> SVGMath.changes
- svgmath.spec -> SVGMath.spec
  Sat Feb 07 22:18:00 CEST 2009 - toms AT suse.de
- Corrected SPEC file to avoid rpmlint warnings
- Used more RPM macros in SPEC file
- SVGMath.changes -> svgmath.changes
  Tue Dec 27 20:40:00 CET 2007 - toms AT suse.de
- Updated to release 0.3.2
- Fixed math2svg.py
- Placed configuration file under /etc/SVGMath
- TODO: svgmath.xml configuration file needs further investigation
  Fri May 18 08:25:00 CET 2007 - toms AT suse.de
  First inital version 0.3.1 on openSUSE build server
