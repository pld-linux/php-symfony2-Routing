%define		package	Routing
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Routing Component
Name:		php-symfony2-Routing
Version:	2.7.5
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	3db222e93df6fb62b627c3caa0b618be
URL:		http://symfony.com/doc/2.7/components/routing/index.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php(tokenizer)
Requires:	php-pear >= 4:1.3.10
Suggests:	php-doctrine-Annotations
Suggests:	php-symfony2-Config
Suggests:	php-symfony2-ExpressionLanguage
Suggests:	php-symfony2-Yaml
Conflicts:	php-symfony2-Config < 2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq_pear	Config.* Yaml.*

%description
The Routing Component maps an HTTP request to a set of configuration
variables.

%prep
%setup -q -n routing-%{version}

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}/Tests
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/Routing
%{php_pear_dir}/Symfony/Component/Routing/*.php
%{php_pear_dir}/Symfony/Component/Routing/Annotation
%{php_pear_dir}/Symfony/Component/Routing/Exception
%{php_pear_dir}/Symfony/Component/Routing/Generator
%{php_pear_dir}/Symfony/Component/Routing/Loader
%{php_pear_dir}/Symfony/Component/Routing/Matcher
