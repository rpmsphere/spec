Name: pywm
Summary: Pythonic window manager
Version: 0.1
Release: 3.1
Group: User Interface/X
License: GPL
URL: http://pywm.sourceforge.net/
Source0: http://sourceforge.net/projects/pywm/files/pywm/0.1-1-a4-1/%{name}-0.1-1-a4-1.tar.bz2
BuildRequires: fltk-devel
BuildRequires: Pyrex

%description
PyWM is a fast, light and flexible window manager for X11 desktops
which is fully (and very easily) scriptable in Python. Automate and
control your desktop to your heart's content.

%prep
%setup -q -n %{name}-0.1-1-a4-1
sed -i 's|fl_xfont==NULL|!fl_xfont|' src-c/Rotated.cpp
sed -i 's|    return 1|return 1|' examples/test.py

%build
export CFLAGS="-Wno-format-security -DFL_INTERNALS -fpermissive"
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc TROUBLESHOOT LICENSE README
%{_bindir}/*
%{python2_sitearch}/*

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1.a4.1
- Rebuild for Fedora
