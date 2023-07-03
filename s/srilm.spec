Name:           srilm
Version:        1.6.0
Release:        6.1
License:        SRILM Research Community License
Group:          Productivity/Scientific/Other 
BuildRequires:  gcc-c++ tcsh tcl-devel
BuildArch:      noarch
URL:            https://www.speech.sri.com/projects/srilm/
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-1.6.0-sanity.patch
Summary:        SRI Language Modeling Toolkit

%description
SRILM is a toolkit for building and applying statistical language models (LMs),
primarily for use in speech recognition, statistical tagging and segmentation,
and machine translation. It has been under development in the SRI Speech
Technology and Research Laboratory since 1995. The toolkit has also greatly
benefitted from its use and enhancements during the Johns Hopkins
University/CLSP summer workshops in 1995, 1996, 1997, and 2002.

%package devel
Summary:        SRI Language Modeling Toolkit development files
License:        SRILM Research Community License
Requires:       srilm
Group:          Productivity/Scientific/Other 

%description devel
SRILM is a toolkit for building and applying statistical language models (LMs),
primarily for use in speech recognition, statistical tagging and segmentation,
and machine translation. It has been under development in the SRI Speech
Technology and Research Laboratory since 1995. The toolkit has also greatly
benefitted from its use and enhancements during the Johns Hopkins
University/CLSP summer workshops in 1995, 1996, 1997, and 2002.

%prep
%setup -q -c
%patch0

%build
sed -i "s|#\ SRILM\ =.*|SRILM\ =\ `pwd`|" Makefile
sed -i "s|.*RPM_FLAGS.*|RPM_FLAGS\ =\ ${RPM_OPT_FLAGS}|" common/Makefile.common.variables
%{__make} MACHINE_TYPE=i686-gcc4 MAKE_PIC=yes World

%install
mkdir -p %{buildroot}%{_bindir}
find bin -type f -exec cp \{\} %{buildroot}%{_bindir} \;
mkdir -p %{buildroot}%{_sbindir}
cp sbin/machine-type %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_includedir}/{%name}
mv include %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_mandir}
mv man/man[0-9] %{buildroot}%{_mandir}
mkdir -p %{buildroot}%{_libdir}
mv lib/*/*.a %{buildroot}%{_libdir}

%clean
%{__rm} -rf %{buildroot}

%files 
%doc doc/README.linux doc/icslp2002-srilm.pdf doc/lm-intro doc/overview doc/FAQ doc/FSM doc/time-space-tradeoff
%{_bindir}/*
%{_mandir}/*/*

%files devel
%{_includedir}/%{name}
%{_libdir}/*.a
%{_sbindir}/*

%changelog
* Sun Jun 30 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.0
- Rebuilt for Fedora
* Tue Jan 31 2012 mhrusecky@suse.cz
- including machine-type into -devel package
* Tue Jan 31 2012 mhrusecky@suse.cz
- updated to version 1.6.0
* Sat Dec  5 2009 mhrusecky@suse.cz
- enabling tcl (thanks to Myroslava Dzikovska for pointing this out)
* Thu Nov 19 2009 mhrusecky@suse.cz
- packaging man pages and static libraries as well
* Sun Oct 25 2009 mhrusecky@suse.cz
- packaged first version of srilm (version 1.5.9)
