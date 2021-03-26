%global debug_package %{nil}

Name: edbrowse
Summary: ed-alike webbrowser written in C
Version: 3.7.4
Release: 7.1
Group: Network
License: Free Software
URL: http://edbrowse.org/
Source0: https://github.com/CMB/edbrowse/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: curl-devel
BuildRequires: readline-devel
BuildRequires: pcre-devel
BuildRequires: libtidy-devel
BuildRequires: duktape-devel

%description
edbrowse is a reimplementation of /bin/ed, with some basic
differences (it uses Perl regular expressions) with the ability to
visit webpages and ftp sites. edbrowse performs basic transformations
on the html source to produce a readable representation. edbrowse
supports Forms, Frames, Netscape-style cookies, HTTPS
connections and JavaScript.

%prep
%setup -q
sed -i '1557d' src/http.c

%build
%cmake
make %{?_smp_mflags}

%install
install -Dm755 src/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README COPYING CHANGES
%{_bindir}/%{name}

%changelog
* Mon Oct 15 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.7.4
- Rebuild for Fedora
