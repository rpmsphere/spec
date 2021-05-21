Name:          python-z3c-rml
Version:       0.9.1
Release:       6.1
Summary:       An alternative implementation of RML
Group:         System/Libraries/Python
URL:           http://pypi.python.org/pypi/z3c.rml
Source:        http://pypi.python.org/packages/source/z/z3c.rml/z3c.rml-%{version}.tar.gz
License:       Zope Public License
BuildRequires: python2-setuptools
BuildRequires:  python2
Requires:      python-reportlab
Requires:      python-zope-schema
Requires:      python-lxml
BuildArch:     noarch

%description
z3c.rml is an alternative implementation of ReportLab's RML PDF generation XML format.
Like the original implementation, it is based on ReportLab's reportlab library.

%prep
%setup -q -n z3c.rml-%{version}

%build
%{__python} setup.py build

%install
rm -rf "$RPM_BUILD_ROOT"
%{__python} setup.py install \
   -O1 --skip-build \
   --root="$RPM_BUILD_ROOT" \
   --install-headers=%{_includedir}/python \
   --install-lib=%{python_sitelib} \
   --single-version-externally-managed \
   --record=%{name}.filelist

#sed -i "\,\.egg-info/,d;s,.*/man/.*,&.gz," %{name}.filelist

echo "#!/bin/sh" > rml2pdf.sh
echo exec "%{__python}" "%{python_sitelib}/z3c/rml/rml2pdf.py" "\$@" >> rml2pdf.sh
install -D -m 755 rml2pdf.sh \
   $RPM_BUILD_ROOT%{_bindir}/rml2pdf
echo "%{_bindir}/rml2pdf" >> %{name}.filelist

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf "$RPM_BUILD_ROOT"

%files -f %{name}.filelist
%doc AUTHORS.txt CHANGES.txt README.txt TODOS.txt

%changelog
* Mon Jun 13 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.1
- Rebuilt for Fedora
* Wed Oct 13 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 0.9.1-1mamba
- package created by autospec
