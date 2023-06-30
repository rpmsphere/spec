%undefine _debugsource_packages

Name: flxlab
Summary: A program for running psychology experiments
Version: 2.5
Release: 6.1
Group: Applications/Engineering
License: GPL
URL: https://flxlab.sourceforge.net/
Source0: https://sourceforge.net/projects/flxlab/files/flxlab/2.5alpha/%{name}-%{version}-src.tar
BuildRequires: allegro-devel
BuildRequires: libX11-devel
BuildRequires: glib2-devel
BuildRequires: alsa-lib-devel

%description
FLXLab is a program for conducting computer-based experiments in psychology and
related fields. It can present stimuli in the form of graphics, text, or sound,
and can record responses to those stimuli, either manual (i.e., pressing a key)
or verbal.

%prep
%setup -q -n %{name}-%{version}-src

%build
export CFLAGS=-fpermissive
perl configure.pl linux
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc README.txt LICENSE.TXT

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5
- Rebuilt for Fedora
