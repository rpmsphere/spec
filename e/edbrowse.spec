%undefine _debugsource_packages

Name: edbrowse
Summary: ed-alike webbrowser written in C
Version: 3.8.1
Release: 1
Group: Network
License: Free Software
URL: https://edbrowse.org/
Source0: https://github.com/CMB/edbrowse/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: modified_runtime.h
BuildRequires: gcc cmake
BuildRequires: curl-devel
BuildRequires: readline-devel
BuildRequires: pcre-devel
BuildRequires: libtidy-devel
BuildRequires: duktape-devel
BuildRequires: quickjs-devel

%description
edbrowse is a reimplementation of /bin/ed, with some basic
differences (it uses Perl regular expressions) with the ability to
visit webpages and ftp sites. edbrowse performs basic transformations
on the html source to produce a readable representation. edbrowse
supports Forms, Frames, Netscape-style cookies, HTTPS
connections and JavaScript.

%prep
%setup -q
#sed -i '1557d' src/http.c
sed -i 's|-L/usr/local/lib/quickjs -lquickjs|%{_libdir}/quickjs/libquickjs.a|' src/makefile
cp %{SOURCE1} src

%build
make %{?_smp_mflags}

%install
install -Dm755 src/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README COPYING CHANGES
%{_bindir}/%{name}

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.8.1
- Rebuilt for Fedora
