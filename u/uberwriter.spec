Name: uberwriter
Summary: A writing application for markdown
Version: 2.1.5a
Release: 1
Group: Applications/Editors
License: GPLv3
URL: http://uberwriter.wolfvollprecht.de/
Source0: https://launchpad.net/uberwriter/trunk/12.11/+download/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel, python3-distutils-extra, intltool

%description
With UberWriter it's simple to write beautiful documents in Markdown.
But UberWriter goes even further: It utilizes pandoc to do the conversion.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%doc AUTHORS COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{python3_sitelib}/*
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/de.wolfvollprecht.UberWriter.svg

%changelog
* Thu Sep 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.5a
- Rebuilt for Fedora
