%global debug_package %{nil}
Name: mimeo
Version: 2015.1
Release: 2.1
Summary: Open files by MIME-type or file name using regular expressions
Group: Utility
License: GPL2
URL: http://xyne.archlinux.ca/projects/mimeo/
Source0: http://xyne.archlinux.ca/projects/mimeo/src/mimeo-2015.1.tar.xz
BuildRequires: python-devel
BuildArch: noarch

%description
Mimeo uses MIME-type file associations to determine which application should
be used to open a file. It can launch files or print information such as the
command that it would use, the detected MIME-type, etc. It is also possible
to use regular expressions to associate arguments with applications. The most
common example is to open URLs in browsers or associate file extensions with
applications irrespective of their MIME-type.

%prep
%setup -q

%install
python2 setup.py install --root=%{buildroot}
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc COPYING CHANGELOG
%{_bindir}/%{name}
%{python2_sitelib}/*

%changelog
* Sat Feb 21 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2015.1
- Rebuild for Fedora
