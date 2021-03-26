%global debug_package %{nil}

Name: akaneclock
Summary: An X Window System analog clock
Version: 0.31
Release: 1
Group: Amusements/Games
License: free
URL: http://rosegray.sakura.ne.jp/software.html#AkaneTokei
Source0: http://rosegray.sakura.ne.jp/%{name}-%{version}.tar.gz
BuildRequires: libXaw-devel libXmu-devel libXt-devel libXext-devel

%description
AkaneClock is an excellent anime clock. Lots more fun to have sitting on your
desktop than the normal clock.

%prep
%setup -q
cp build/Imakefile.1 Imakefile

%build
xmkmf -a
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc README*
%{_bindir}/%{name}

%changelog
* Wed Dec 18 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.31
- Rebuild for Fedora
