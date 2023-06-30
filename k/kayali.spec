Name: kayali
Summary: A Qt-based Computer Algebra System
Version: 0.3.2
Release: 4.1
Group: Applications/Engineering
License: GPL
URL: https://kayali.sourceforge.net/
Source0: https://jaist.dl.sourceforge.net/project/kayali/kayali/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
BuildArch: noarch
Requires: PyQt4, maxima, gnuplot, ImageMagick, gd
#Requires: python-yapps, pexpect, python-reportlab

%description
Kayali is a Qt based Computer Algebra System (CAS) that can also be used
as an advanced replacement for KDE KCalc. It is essentially a front end GUI
for Maxima (and is easily extended to other CAS back-ends) and Gnuplot.

%prep
%setup -q -n %{name}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
python2 %{name}.py
EOF
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/%{name}.py

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Nov 04 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2
- Rebuilt for Fedora
