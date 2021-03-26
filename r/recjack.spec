Name: recjack
Summary: A graphical user interface for jack_capture
Version: 0.2.1
Release: 3.1
Group: Converted/sound
License: see /usr/share/doc/recjack/copyright
URL: http://mein-neues-blog.de/category/recjack/
Source0: http://repository.mein-neues-blog.de:9000/archive/%{name}-%{version}_all.tar.gz
BuildArch: noarch
BuildRequires: desktop-file-utils

%description
RecJack is a front end for jack_capture. This tool is used to record
the output of a jack server to a file. RecJack provides the most significant
features of jack_capture in an easy-to-use graphical user interface.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}
cp -a * %{buildroot}

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/doc/%{name}
%{_datadir}/pixmaps/*

%changelog
* Wed May 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1
- Rebuild for Fedora
