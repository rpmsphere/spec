%global debug_package %{nil}
Name:           latexslides
Version:        0.31
Release:        3.1
Summary:        Generating presentations in LaTeX using Python code
Group:          Development/Languages/Python
License:        New BSD
URL:            http://code.google.com/p/latexslides/
Source0:        http://latexslides.googlecode.com/files/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2

%description
Latexslides is a tool that allows you to write slides in Python: each slide is
a Python object, and a talk is a list of such objects. This list can converted
to LaTeX beamer or prosper code. One can compose talks by importing slide
objects from Python modules and hence reuse individual slides.

%prep
%setup -q

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install -O1 --skip-build --prefix=/usr --root $RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGELOG README TODO doc/*
%{_bindir}/*
%{python2_sitelib}/*
%{_datadir}/texmf/tex/latex/%{name}

%changelog
* Mon Jun 18 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.31
- Rebuild for Fedora
