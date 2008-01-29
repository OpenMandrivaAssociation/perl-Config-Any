%define module	Config-Any
%define name	perl-%{module}
%define	modprefix Config

%define version	0.11
%define	rel	1
%define release	%mkrel %{rel}

Summary:	Load configuration from different file formats, transparently
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
BuildRequires:  perl(Module::Pluggable) >= 3.01
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-version
BuildArch:	    noarch
Buildroot:	    %{_tmppath}/%{name}-%{version}

%description
Config::Any provides a facility for Perl applications and libraries to
load configuration data from multiple different file formats. It
supports XML, YAML, JSON, Apache-style configuration, Windows INI
files, and even Perl code.


%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

%clean
rm -rf %{buildroot}


