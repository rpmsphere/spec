%undefine _debugsource_packages
Name:           python-pyfann
Version:        2.1.0beta
Release:        9.1
License:        MIT
Summary:        Python bindings for FANN
URL:            https://code.google.com/p/fann-python25/
Group:          Development/Languages/Python
Source:         pyfann-2.1.0.zip
BuildRequires:  python2-devel, swig, fann-devel

%description
Fast Artificial Neural Network (FANN) Library is written in ANSI C.
The library implements multilayer feedforward ANNs, up to 150 times faster
than other libraries. FANN supports execution in fixed point, for fast
execution on systems like the iPAQ.

%prep
%setup -q -c
sed -i 's|\.\./\.\./src|/usr|' pyfann/pyfann.i
sed -i 's|\.\./src/doublefann\.o|-ldoublefann|' setup.py

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%{python2_sitearch}/*

%changelog
* Sun Jun 16 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0beta
- Rebuilt for Fedora
