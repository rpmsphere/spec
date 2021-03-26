Version: 0.2.3
Release: 1
Name: udev-discover
Summary: A tool for helping browsing the sysfs tree via udev
License: GPLv3+
Group: System/Configuration/Hardware
URL: https://github.com/fontanon/udev-discover
Source0: %name-%version.tar
BuildArch: noarch
BuildRequires: python-devel
#BuildRequires: python-module-pygobject-devel
#BuildRequires: python-module-gudev
#BuildRequires: libgtk+3-gir-devel

%description
A tool for helping browsing the sysfs tree via udev focused on being
helpfull for udev testers, coders, hackers and consumers.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%doc AUTHORS README.rst TODO
%_bindir/*
%_sysconfdir/gconf/schemas/*.schemas
%python_sitelib/*
%_datadir/applications/*.desktop
%_datadir/icons/hicolor/*/*/*.svg
%_datadir/locale/*/LC_MESSAGES/*.mo
%_datadir/pixmaps/*.svg
%_datadir/%name

%changelog
* Tue Feb 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.3
- Rebuild for Fedora
* Fri Sep 12 2014 Cronbuild Service <cronbuild@altlinux.org> 0.2.3-alt1
- Freshed up to v0.2.3 with the help of cronbuild and update-source-functions.
* Wed Dec 25 2013 Paul Wolneykien <manowar@altlinux.org> 0.2.2-alt1
- Freshed up to v0.2.2 with the help of cronbuild and update-source-functions.
