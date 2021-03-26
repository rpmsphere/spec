%global debug_package %{nil}

Name:         rdup
Summary:      Filesystem Tree Change Discovery Tool
URL:          http://www.miek.nl/projects/rdup/
Group:        Filesystem
License:      GPL
Version:      1.1.15
Release:      1
Source0:      http://www.miek.nl/projects/rdup/rdup-%{version}.tar.gz
BuildRequires: glib2-devel
BuildRequires: pcre-devel

%description
rdup(1) is a utility inspired by rsync(1) and the Plan9 way of doing
backups. rdup(1) itself does not backup anything. It only prints a
list of files that are changed, or all files in case of a null dump,
to standard output. Subsequent programs in a pipe line can be used
to actually implement to backup scheme. After a run a new filelist
is written. No warning is given when filelist is an existing file,
it just gets overwritten by rdup. New runs will print out only those
files that have actually changed since the last run, thereby making
incremental backups possible.

%prep
%setup -q
sed -i 's|-Werror||' GNUmakefile*

%build
autoreconf -ifv
./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir}
%{__make}

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_mandir}/man?/*

%changelog
* Mon Oct 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.15
- Rebuild for Fedora
