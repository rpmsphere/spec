Summary:    A filter for gcc diagnostic messages
Name:       gccfilter
Version:    2010
Release:    4.1
License:    free software
Group:      Development/Tools
URL:        https://www.mixtion.org/gccfilter/
Source0:    https://www.mixtion.org/gccfilter/gccfilter
Source1:    https://www.mixtion.org/gccfilter/gccfilter.html
BuildArch:  noarch
Requires:   perl(Term::ANSIColor)
Requires:   perl(Getopt::ArgvFile)
Requires:   perl(Getopt::Long)
Requires:   perl(Regexp::Common)

%description
gccfilter is a perl filter to colorize and simplify (or expand) gcc diagnostic
messages. gccfilter is particularly aimed at g++ (i.e. dealinging with C++)
messages which can contain lot of template-related errors or warnings difficult
to sort out. 

%prep
%setup -T -c
cp %{SOURCE0} %{SOURCE1} .

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -p -m 755 %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}

%files
%doc %{name}.html
%{_bindir}/%{name}

%changelog
* Sun Nov 18 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2010
- Rebuilt for Fedora
