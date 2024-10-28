%undefine _debugsource_packages
Name:           python-pymmlib
Version:        1.2.0
Release:        8.1
Summary:        Python Macromolecular Library
Group:          Libraries/Sciences/Crystallography
License:        Artistic License
URL:            https://pymmlib.sourceforge.net/
Source0:        https://downloads.sourceforge.net/pymmlib/pymmlib-%{version}.tar.gz
BuildRequires:  python2-devel numpy pygtk2-devel atlas
#BuildRequires:  python2-pyopengl pygtkglext-devel

%description
The Python Macromolecular Library (mmLib) is a collection of Python
modules the examination and manipulation of macromolecular structures,
and the files which describe them.

%prep
%setup -q -n pymmlib-%{version}

%build
export CFLAGS="${RPM_OPT_FLAGS}"
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --root=$RPM_BUILD_ROOT

# Monomer library is provided by a separate package
#grep -v Monomers pymmlib.list.orig | sed -e /\.pyc$/d -e s,\.py$,\.py\*,g > pymmlib.list
#rm -rf $RPM_BUILD_ROOT%{python2_sitelib}/mmLib/Data/Monomers

# install applications
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for i in applications/* ; do
  install -m 755 ${i} $RPM_BUILD_ROOT%{_bindir}/`basename ${i} .py`
done

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc AUTHORS.txt LICENSE.txt README.txt doc examples tests
%{_bindir}/*
%{python2_sitearch}/*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuilt for Fedora
* Fri Aug  3 2007 MATSUURA Takanori <t.matsuu at gmail.com> - 1.0.0-1
- initial build
