%define upstream_name	 Config-Any
%define upstream_version 0.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Load configuration from different file formats, transparently
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Module::Pluggable) >= 3.01
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Config::General)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(JSON)
BuildRequires:  perl(YAML)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl-version

BuildArch:	    noarch
Buildroot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
Config::Any provides a facility for Perl applications and libraries to
load configuration data from multiple different file formats. It
supports XML, YAML, JSON, Apache-style configuration, Windows INI
files, and even Perl code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Config
