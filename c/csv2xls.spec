Name:          csv2xls
Version:       0.4.2
Release:       3.1
Summary:       A command line utility that enables the creation of xls files across platforms 
Group:         Applications/File 
URL:           http://sourceforge.net/projects/py-csv2xls/ 
Source:        http://downloads.sourceforge.net/project/py-csv2xls/py-csv2xls/%{version}/csv2xls-%{version}.tgz
License:       MIT
BuildRequires: pyexcelerator
Requires:      pyexcelerator
BuildArch:     noarch

%description
CSV2XLS is a command line utility that enables the creation of xls files
across platforms. It supports multiple sheets, formatting, and the choice
of fonts.

%prep
%setup -q
sed -i "s, \(%{_bindir}/\), $RPM_BUILD_ROOT\1,;s,\(/opt\),%{buildroot}%{_datadir}," configure
sed -i "s,\(py\)exc,\1Exc,g" src/csv2xls.py
sed -i "s,/opt,%{_datadir}," src/csv2xls
sed -i 's|python |python2 |' configure src/csv2xls.py src/csv2xls
sed -i 's|/usr/bin/env python|/usr/bin/python2|' */*.py

%build
./configure

%install
rm -rf $RPM_BUILD_ROOT
tar -xjf tarballs/external.bz2
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/csv2xls
cp -pr afm \
  $RPM_BUILD_ROOT%{_datadir}/csv2xls/
cp -pr Adobe-Core35_AFMs-314 \
  $RPM_BUILD_ROOT%{_datadir}/csv2xls/
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_datadir}/csv2xls/afm/LICENSE*
rm -f $RPM_BUILD_ROOT%{_datadir}/csv2xls/Adobe-Core35_AFMs-314/{LICENSE,*.html}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/csv2xls
%{_datadir}/csv2xls
%doc LICENSE README

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuilt for Fedora
* Tue Jan 05 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 0.4.2-2mamba
- added missing requirement
* Tue Jan 05 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 0.4.2-1mamba
- package created by autospec
